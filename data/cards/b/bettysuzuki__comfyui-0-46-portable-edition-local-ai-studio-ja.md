# bettysuzuki/comfyui-0-46-portable-edition-local-ai-studio-ja

⭐ 14 · Python · NOASSERTION · 推送 2026-11-26 · [GitHub](https://github.com/bettysuzuki/comfyui-0-46-portable-edition-local-ai-studio-ja) · [官网](https://bettysuzuki.github.io/comfyui-0-46-portable-edition-local-ai-studio-ja/) · 个人维护

**Windows 便携版 ComfyUI 0.46 本地 AI 图像生成套件**

面向 Windows 10/11（x64）用户分发的 ComfyUI 0.46 便携预配置版本：将运行时库、GPU 加速钩子（CUDA/Vulkan/DirectX 12）与插件桥预链接在独立目录内，解压即用、无注册表写入。通过发布页下载 AES-256 加密 zip（密码 2026）后以管理员身份启动主程序。README 未包含模型权重获取、节点工作流配置等内容，仅描述便携包结构与启动步骤。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 预链接 CUDA/Vulkan/DirectX 12 GPU 加速钩子的便携目录
- 无注册表写入，可从任意 SSD/NVMe 文件夹直接运行
- 提供 SHA-256 完整性校验入口
- 卸载方式为删除解压目录，不改系统文件

## 适用场景

- 在 Windows 上便携运行 ComfyUI 生成图像
- 不污染系统注册表的本地 AI 图像生成环境

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L21: **comfyui-0-46-portable-edition-local-ai-studio-ja** is a pre-configured, self-contained Windows 10/11 (x64) workst
> L23: All core runtime libraries, GPU hardware acceleration hooks (CUDA / Vulkan / DirectX 12), and plugin bridges are pr


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 mid · 依据 README sha `e520d4757efb` · [字段定义](../../DATASET.md)*
