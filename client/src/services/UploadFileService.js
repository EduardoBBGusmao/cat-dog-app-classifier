import http from "../http-common";

class UploadFilesService {
  upload(file) {
    const formData = new FormData();

    formData.append("animal", file);

    return http.post("/polls", formData, {
      headers: {
        "Content-Type": "multipart/form-data"
      }
    });
  }
}

export default new UploadFilesService();