class PlayersController < ApplicationController
  include ApiHelper
  def create
    key = params["player"]["key"]
    response =  api_call(2, "user", "", key)
    # Call Torn's API /user, if we get a good response the key is valid

    if response["error"].blank?
    # TODO: Create account and loging

    else
      # TODO: Return error to user and redirect to new
    end
  end


  def new
    # TODO: if player is logged in, redirect to dashboard
    @player = Player.new
  end
end
