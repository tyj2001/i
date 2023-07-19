import requests
import json

def imagine_picture(prompt):
    url = "http://midjourney-api.ai-des.com/func2api/Imagine"
    headers = {
        "Content-Type": "application/json",
        "UUID": "afd22831-6e9e-c4e4-2477-825a3328a178"
    }
    data = {
        "type": "P",
        "prompt": prompt,
        "imgId": "",
        "num": 0
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()["data"]["imgId"]
    else:
        return None

def get_picture_url(img_id):
    url = "http://midjourney-api.ai-des.com/func2api/GetPicByImgID"
    headers = {
        "Content-Type": "application/json",
        "UUID": "afd22831-6e9e-c4e4-2477-825a3328a178"
    }
    data = {
        "imgId": img_id
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    print(f"Status code: {response.status_code}")
    print(f"Response content: {response.content}")  # This will print the entire response
    if response.status_code == 200:
        return response.json()["data"]["url"]
    else:
        return None

def main():
    prompt = "一个企鹅，骑着摩托，抱着狗"
    img_id = imagine_picture(prompt)
    if img_id:
        url = get_picture_url(img_id)
        if url:
            with open('image_url.txt', 'w') as file:
                file.write(url)
        else:
            print("Failed to get image URL.")
    else:
        print("Failed to generate image.")

if __name__ == "__main__":
    main()
