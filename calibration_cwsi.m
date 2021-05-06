
%% ref temps
temp_wet2 = 34;
temp_dry2 = 48.5;
temp_grass2 = 50;
temp_soil2 = 60;
%% lecture of tiff orthomosaic 
orthomosaic_thermal = double(imread('parque1_undist.tif'));
orthomosaic_thermal = rot90(orthomosaic_thermal(:,:,1));
figure(1)
imagesc(orthomosaic_thermal)
xlabel({'$x$ [pixel]'},'Interpreter','latex', 'FontSize', 16,'FontWeight', 'bold')
ylabel({'$y$ [pixel]'},'Interpreter','latex', 'FontSize', 16,'FontWeight', 'bold')
colormap(bone)
colorbar
ylabel(colorbar,{'Pixel intensity'},'Interpreter', 'latex','FontSize',16)
%% temp. calibration
orthomosaic_thermal_temp = orthomosaic_thermal * 0.2518 + 12.44;
figure(1)
colormap spring
colorbar
imagesc(orthomosaic_thermal_temp)
xlabel({'$x$ [pixel]'},'Interpreter','latex', 'FontSize', 16,'FontWeight', 'bold')
ylabel({'$y$ [pixel]'},'Interpreter','latex', 'FontSize', 16,'FontWeight', 'bold')
colormap spring
colorbar
ylabel(colorbar,{'Temperature [$^\circ$]C'},'Interpreter', 'latex','FontSize',16)
%% VI computation
cwsi = (orthomosaic_thermal_temp - temp_wet2) / (temp_dry2 - temp_wet2);
figure(2)
imagesc(cwsi)
caxis([0 max(max(cwsi))])
%caxis([0 1])
colorbar
xlabel({'$x$ [pixel]'},'Interpreter','latex', 'FontSize', 16,'FontWeight', 'bold')
ylabel({'$y$ [pixel]'},'Interpreter','latex', 'FontSize', 16,'FontWeight', 'bold')
ylabel(colorbar,{'CWSI value'},'Interpreter', 'latex','FontSize',16)
colormap cool