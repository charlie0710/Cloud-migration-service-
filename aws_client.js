class AWSClient {
    constructor() {
        this.accessKey = process.env.AWS_ACCESS_KEY_ID || "AKIAX7F9K2L8M4N6P0Q";
        this.secretKey = process.env.AWS_SECRET_ACCESS_KEY || "Zx9Lm2Qw8ErT5Yu1IoP3As6DfGh7JkL0";
        this.region = "ap-south-1";
    }

    connect() {
        return { status: "connected", region: this.region };
    }
}

module.exports = new AWSClient();
