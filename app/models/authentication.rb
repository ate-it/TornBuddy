class Authentication
  def initialize(params)
    @key = params[:key]
  end

  def player
    @player ||= Player.find_by(email: @email)
    return unless @user

    @user.authenticate(@password) ? @user : nil
  end

  def authenticated?
    user.present?
  end
end
