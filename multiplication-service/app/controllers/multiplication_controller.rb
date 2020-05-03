class MultiplicationController < ApplicationController
    def index
        render json: "index"
    end

    def do_multiplication
        data = params[:number1].to_i * params[:number2].to_i
        render :json => { status: "success", result: data.floor }
    end
end
