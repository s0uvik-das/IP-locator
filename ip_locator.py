import requests
import sys

def api(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        response.raise_for_status()
        fetch_data = response.json()
        
        print(f"Retrieving information for IP: {ip}")
        print()
        
        if fetch_data.get("status") == "success":
            print(f"IP : {ip}")
            print(f"Country : {fetch_data.get('country', 'N/A')}")
            print(f"CountryCode : {fetch_data.get('countryCode', 'N/A')}")
            print(f"Region : {fetch_data.get('region', 'N/A')}")
            print(f"Region Name : {fetch_data.get('regionName', 'N/A')}")
            print(f"City : {fetch_data.get('city', 'N/A')}")
            print(f"Zip Code : {fetch_data.get('zip', 'N/A')}")
            print(f"Latitude : {fetch_data.get('lat', 'N/A')}")
            print(f"Longitude : {fetch_data.get('lon', 'N/A')}")
            print(f"Time-zone : {fetch_data.get('timezone', 'N/A')}")
            print(f"ISP : {fetch_data.get('isp', 'N/A')}")
            print(f"Organization : {fetch_data.get('org', 'N/A')}")
            print(f"Autonomous System Number : {fetch_data.get('as', 'N/A')}")
            print()
            print("Successfully retrieved IP information . . .\n")
        else:
            print(f"Error retrieving data for {ip}: {fetch_data.get('message', 'Unknown error')}")
    
    except requests.exceptions.RequestException as e:
        print(f"Request error for {ip}: {e}")
    
    except ValueError:
        print(f"Error parsing JSON response for {ip}.")
    
    except KeyError as e:
        print(f"Missing key in response for {ip}: {e}")
    
    except Exception as e:
        print(f"An unexpected error occurred for {ip}: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("At least one ip required")
        print("Usage: python script.py <IP1> <IP2> ... <IPn>")
    else:
        ips = sys.argv[1:]
        for ip in ips:
            api(ip)

