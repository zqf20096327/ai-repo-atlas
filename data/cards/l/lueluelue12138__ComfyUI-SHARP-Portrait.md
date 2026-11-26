# lueluelue12138/ComfyUI-SHARP-Portrait

⭐ 11 · JavaScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/lueluelue12138/ComfyUI-SHARP-Portrait) · 个人维护 · 中文 README

**ComfyUI 节点包：单张人物照片换视角生成与细节精修**

作为 ComfyUI 自定义节点运行：将人物照片经 Apple SHARP 建成高斯模型，在 3D 相机中拖动取景换角度，再用 Qwen Image 2.1 Turbo INT8 与 Splat Repair LoRA 修补缺损、按原图或特写参考精修细节；支持遮罩精修、dolly zoom、关键帧轨迹逐帧导出与 transforms.json 保存。开发验证环境为 Windows、Python 3.12、12 GB 显存、NVIDIA CUDA，其他平台未验证；未见区域由模型推测，跨角度一致性需按素材验证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单图建高斯后 3D 相机交互取景，支持旋转中心选取与镜头转角扶正
- Qwen + Splat Repair 修补新机位缺损，双图参考与自由遮罩精修细节
- 相机关键帧补间、逐帧导出粗图或修复图并保存 transforms.json
- 提供 Sharp GUI 图库工作台接入同一工作流

## 适用场景

- 把一张人像照片转成多个机位的成图
- 对换视角后的脸部、服饰细节做遮罩精修
- 导出相机轨迹序列帧与相机参数

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L1: # ComfyUI SHARP Portrait · 单图人物换视角
> L3: **Interactive single-photo portrait novel-view synthesis with Apple SHARP, Gaussian splatting, Qwen-Image 2.1 Turbo 
> L64: ## 功能
> L79: 已验证开发环境为 Windows、Python 3.12、NVIDIA CUDA、ComfyUI 0.42.5、前端 1.55.18，使用 12 GB 显存笔记本。其他平台尚未验证。高分辨率与大参考图会增加内存、显存及时间开销。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `3f0fee72723f` · [字段定义](../../DATASET.md)*
