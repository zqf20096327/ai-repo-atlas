# gahingwoo/kiln

⭐ 12 · Shell · GPL-2.0 · 推送 2026-08-13 · [GitHub](https://github.com/gahingwoo/kiln) · [官网](https://docs.radxa.com/en/rock4/rock4d/application-dev/npu/kiln) · 个人维护 · 中文 README

**在 RK3576 NPU 主线内核上运行本地 LLM 与视觉推理**

面向 Radxa ROCK 4D（RK3576/Armbian）的本地离线 AI 部署工具：通过 out-of-tree 构建 rknpu 内核驱动并叠加 10 个主线内核补丁（时钟/电源域/双 IOMMU），使厂商 RKLLM/RKNN 栈脱离 6.1 BSP、运行在主线 linux-7.1.3 内核上。提供一条命令安装脚本（自动重启两次完成部署），附带 kiln-chat 多轮对话 CLI、kiln-vision 图像分类/检测、kiln-serve 的 OpenAI 兼容 HTTP API、板上模型转换与健康检查工具。仅测试过单一硬件型号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | GPL-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 厂商 RKLLM/RKNN 栈经补丁后运行于主线内核（out-of-tree rknpu 驱动 + 10 个内核补丁）
- kiln-serve 提供 OpenAI 兼容 API（SSE 流式），可接入 Open WebUI/LangChain/任意 OpenAI 客户端
- kiln-convert 在板上完成 .rknn/.rkllm 模型转换，无需 x86 主机
- 实测 Qwen2.5-1.5B 约 9 tok/s、Llama-3.2-1B 约 13 tok/s，图像分类约 169 fps

## 适用场景

- 在 ROCK 4D 主线内核上跑离线 LLM 对话，数据不出设备
- 为本地 LLM 提供OpenAI 兼容 API 供现有客户端调用
- 在开发板上直接转换 MobileNet/YOLO 模型做图像分类与检测

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L8: It's exposed as an **OpenAI-compatible API**, so you can point **Open WebUI** (a
> L104: - **`kiln-serve`** — an **OpenAI-compatible** HTTP API for the LLM. Point the
> L117: - **`kiln-chat`** — the interactive LLM CLI. Runs any RKLLM `.rkllm` model; the chat


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `16088910016d` · [字段定义](../../DATASET.md)*
