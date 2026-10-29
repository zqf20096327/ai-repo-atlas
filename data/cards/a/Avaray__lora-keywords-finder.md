# Avaray/lora-keywords-finder

⭐ 24 · Python · MIT · 推送 2026-09-18 · [GitHub](https://github.com/Avaray/lora-keywords-finder) · 个人维护

**ForgeUI/A1111 扩展：查询 CivitAI API 查找本地 LoRA 的触发词**

面向 Forge Neo 及其他基于 AUTOMATIC1111 的 WebUI 的浏览器扩展：用户在 txt2img/img2img 页选择本地 LoRA 文件后，通过 SHA-256 哈希查询 CivitAI API，返回训练关键词、示例图、基础模型版本、下载链接等元数据；示例图可一键发送正向/负向提示词到当前输入框。数据本地缓存供离线访问，支持 safetensors/ckpt/pt/gguf/onnx 格式。限制：仅适用于公开于 CivitAI 的模型，API 宕机时无法获取新数据。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 按哈希查询 CivitAI API 获取 LoRA 训练关键词与示例图
- 示例图提示词一键发送到 txt2img/img2img 输入框
- 数据本地缓存，支持离线再次访问
- 支持 .safetensors/.ckpt/.pt/.gguf/.onnx 文件格式

## 适用场景

- 在 WebUI 里快速查看本地 LoRA 对应的触发词
- 浏览 LoRA 的 CivitAI 示例图并把提示词填入生成框
- 查看本地模型的基础模型版本与下载链接等元数据

## 场景标签

 · 领域:图像生成工具/SD 生态

## 证据(README 行号)

> L5: This Extension lets you easily find trained keywords, example images, and metadata for your local LoRA) models by qu
> L37: 1. The extension will be visible in your **txt2img** and **img2img** tabs under the **🧙 LoRA Keywords Finder** acco

## 星数曲线

```mermaid
xychart-beta
    title "Avaray/lora-keywords-finder 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-29 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `a4c259874b34` · [字段定义](../../DATASET.md)*
