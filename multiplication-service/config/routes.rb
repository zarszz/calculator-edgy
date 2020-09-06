Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  get '/', to: 'multiplication#index'
  post '/multiplication', to: 'multiplication#do_multiplication'
end
