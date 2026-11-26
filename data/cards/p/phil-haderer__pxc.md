# phil-haderer/pxc

⭐ 29 · Python · Apache-2.0 · 推送 2026-11-25 · [GitHub](https://github.com/phil-haderer/pxc) · 个人维护

**为 PhotoCraft 用户提供本地 AI 生图与图像编辑的伴随应用**

一个与 PhotoCraft 图像编辑器配合的伴随应用：用户在自身电脑上通过 ComfyUI 运行本地模型，提供文生图、扩图、填充、移除、编辑、精修、放大七种生成模式，结果作为新图层写回 PhotoCraft 文档。内置七个可下载的模型包（自动分发到 ComfyUI 目录）、LLM 辅助的提示词改写与图像描述、83+34 个风格预设、提示词保存复用，并支持多台客户端共用一台 ComfyUI 服务器的团队队列模式。要求 8 GB VRAM 以上 GPU，双许可 MIT 或 Apache-2.0。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 七种生成模式：文生图、扩图、填充、移除、编辑、精修、放大
- 七个本地模型一键下载并自动放入 ComfyUI 对应文件夹
- LLM 辅助提示词优化、画布描述与草图转提示词
- 支持多客户端共用一台 ComfyUI 服务器并显示队列

## 适用场景

- 在 PhotoCraft 中用提示词生成图像并自动落为新图层
- 对选区做本地 AI 填充、移除或扩图
- 小团队共用一台 GPU 服务器跑 ComfyUI 生图任务

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L7: **A companion app that brings Photoshop-style generative AI to PhotoCraft, running on your own PC.**
> L8: Pick a function, type a prompt, press Generate: the result arrives as a new layer in your document.
> L90: - **PxC** (this companion app, a small window of its own next to PhotoCraft) sits between them: it sends your pictu


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `0215dfc23c02` · [字段定义](../../DATASET.md)*
