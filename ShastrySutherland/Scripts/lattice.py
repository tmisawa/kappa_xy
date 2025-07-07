def site2d_ymajor(all_i,Lx,Ly,orb_num):
  orb  = all_i%orb_num
  site = int((all_i-orb)/orb_num)
  y    = site%Ly
  x    = int((site-y)/Ly)
  if((x)%2==1):
     orb  = (orb+2)%orb_num
  return x,y,orb

def get_allj(all_i,dx,dy,orb_j,Lx,Ly,orb_num):
  x,y,orb = site2d_ymajor(all_i,Lx,Ly,orb_num)
  x_j   = int((x+dx)%Lx)
  y_j   = int((y+dy)%Ly)
  if((x_j)%2==1):
     orb_j  = (orb_j+2)%orb_num
  all_j = orb_j+(y_j+x_j*Ly)*orb_num # y-major
  return all_j
