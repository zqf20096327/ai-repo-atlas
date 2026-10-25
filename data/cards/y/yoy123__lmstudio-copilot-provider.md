# yoy123/lmstudio-copilot-provider

⭐ 39 · TypeScript · MIT · 推送 2026-10-01 · [GitHub](https://github.com/yoy123/lmstudio-copilot-provider) · [官网](https://github.com/yoy123/lmstudio-copilot-provider#readme) · 个人维护

**在 VS Code Copilot Chat 中接入本地 LM Studio 模型的扩展**

VS Code 扩展，将 LM Studio 本地或远程服务器上的模型加入 Copilot Chat 的模型选择器，支持流式响应、工具调用、实验性行内补全（ghost text），以及通过 DALL-E 兼容或 A1111 端点生成图片。本地安装时可自动启动 LM Studio 并懒加载所选模型，自动探测随 LM Studio 附带的 CLI（lms）；远程服务器场景（含 SSH 隧道）可跳过本地 CLI 操作。从 VS Code Marketplace 或 Open VSX 安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 将 LM Studio 模型加入 Copilot Chat 模型选择器并流式输出
- 本地自动启动 LM Studio 服务器与懒加载模型
- 支持远程 LM Studio 服务器与 SSH 隧道场景（treatAsRemote）
- 可选工具调用、行内补全（实验性）与 DALL-E/A1111 图像生成

## 适用场景

- 在 VS Code Copilot Chat 中使用本地模型，减少对云端服务的依赖
- 连接部署在专用服务器或容器中的 LM Studio 实例
- 为支持工具调用的本地模型启用终端/文件类工具

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L14: - Adds LM Studio models to the Copilot Chat model picker
> L31: 3. Pick an LM Studio model.

## 星数曲线

```mermaid
xychart-beta
    title "yoy123/lmstudio-copilot-provider 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-25 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `3e36621be7c1` · [字段定义](../../DATASET.md)*
