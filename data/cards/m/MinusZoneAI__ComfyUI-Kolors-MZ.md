# MinusZoneAI/ComfyUI-Kolors-MZ

⭐ 575 · Python · GPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/MinusZoneAI/ComfyUI-Kolors-MZ) · 个人维护 · 中文 README

**ComfyUI 的 Kolors 文生图原生采样器节点集**

在 ComfyUI 中以原生采样方式实现 Kolors 文生图模型的插件，提供 UNET 加载、ChatGLM3 文本编码（含 V2 高级节点）、ControlNet 加载与 Patch、IPAdapter/ FaceID 相关加载与应用节点，附示例工作流与常见错误排查。用户需自行从 Hugging Face 下载 UNET、ChatGLM3、IPAdapter、ControlNet、Inpainting 等模型并放置到对应 models 文件夹；Mac 用户被指向另一分支仓库。实现参考自 ComfyUI-KwaiKolorsWrapper。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 提供 Kolors 的 ComfyUI 原生采样节点实现
- 包含 ChatGLM3 文本编码节点（含 V2 版本）与 ControlNet 加载/Patch 节点
- 支持 IPAdapter 与 IPAdapter FaceID 的加载与应用节点
- 提供示例工作流与同种子对比测试工作流

## 适用场景

- 在 ComfyUI 工作流中使用 Kolors 生成图像
- 结合 ControlNet 做深度/边缘/姿态控制生成
- 用 IPAdapter FaceID 做人脸相关的图像生成

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L17: ## ComfyUI上Kolors的实现
> L21: 使用ComfyUI原生采样
> L23: 工作流在examples/workflow.png中获取


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 mid · 依据 README sha `dc1d3f5372ec` · [字段定义](../../DATASET.md)*
