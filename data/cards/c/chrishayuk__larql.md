# chrishayuk/larql

⭐ 1,196 · Rust · Apache-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/chrishayuk/larql) · [官网](https://vindex3.org) · 个人维护

**Rust 模型运行时：运行/服务/查询/编辑模型并可观察内部**

用 Rust 编写的模型运行时，基于可执行且可检查的 VINDEX3 模型格式：从 Hugging Face 下载模型并转换缓存后，可运行对话、以 OpenAI 兼容 API 提供服务、用 LQL 查询语言推断与捕获激活/权重、以补丁形式对运行中会话做权重编辑并可导出 GGUF。提供预编译二进制（macOS Apple Silicon/Windows）与源码构建两种安装方式；macOS 构建使用 Metal，另有可移植 CPU 后端。已端到端支持 Qwen3、Gemma 3/4、Granite 4.1。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- LQL 查询语言：推断、观察各层贡献、捕获激活/权重到 NumPy 文件
- 以 .vlp 补丁对运行中会话做权重编辑，可撤销、可编译为新的 VINDEX3 并导出 GGUF
- OpenAI 兼容 API 服务（larql serve）
- 运行前检查模型各部分是否可运行，缺失则拒绝并列出缺失项
- 提供预编译二进制与 Python 绑定

## 适用场景

- 本地运行 Hugging Face 模型并通过 OpenAI 兼容 API 提供给应用或 agent
- 机械可解释性研究：观察各层贡献、导出激活与权重
- 实验性权重编辑并导出到 llama.cpp 或 Ollama 使用
- 量化压缩模型并测量代价

## 场景标签

`推理引擎` `模型量化` · 领域:训练与推理

## 证据(README 行号)

> L5: LARQL is a model runtime written in Rust. Point it at a Hugging Face model and
> L75: **2. Serve it** over an OpenAI-compatible API:

## 星数曲线

```mermaid
xychart-beta
    title "chrishayuk/larql 星数(近 7 点)"
    x-axis ["2026-11-08", "2026-11-10", "2026-11-18", "2026-11-19", "2026-11-20", "2026-11-21", "2026-11-22"]
    y-axis "stars" 1172 --> 1198
    line [1174, 1175, 1179, 1185, 1193, 1195, 1196]
```

2026-11-08 1,174 → 2026-11-22 1,196（+22）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-17 · 置信度 high · 依据 README sha `b1683a4e0178` · [字段定义](../../DATASET.md)*
