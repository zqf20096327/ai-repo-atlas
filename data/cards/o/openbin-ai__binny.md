# openbin-ai/binny

⭐ 180 · Go · AGPL-3.0 · 推送 2026-10-17 · [GitHub](https://github.com/openbin-ai/binny) · [官网](https://openbin.ai/#binny) · 组织维护

**逆向工程 agent 运行框架：接入任意模型分析二进制并产出报告**

BINNY 是一个开源的逆向工程 agent harness（本体是框架，不含模型）：接入 Claude、GPT、DeepSeek、Qwen、Kimi、Gemini、Bedrock 或经 Ollama/LM Studio/llama.cpp/vLLM 运行的本地模型，对 OpenBin/OpenAPK 项目或磁盘上的文件执行 triage→调查→撰写草稿的循环。提供本地 Ghidra 反编译、无网络 Docker 沙箱脚本执行、字符串/导入/函数读取工具、预算与检查点、可恢复会话，草稿落地到项目报告供人工审阅。macOS/Linux/Windows 提供安装脚本与预编译二进制，亦可 Go 1.22 从源码构建；Docker 仅在本地反编译与沙箱时需要。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- triage（STIX 2.1 分类）→调查→草稿的完整分析循环，三种自主级别
- 本地 Ghidra 反编译与无网络 Docker 沙箱（只读根、能力剥离、资源限制）
- 预配置 Anthropic/OpenAI/DeepSeek/Qwen/Kimi/Gemini/Bedrock 及 Ollama/LM Studio/llama.cpp/vLLM 本地后端
- 会话逐步自动保存，可恢复；草稿需人工审阅后才推送

## 适用场景

- 用自带 API key 或本地模型对恶意样本做自动化逆向分析
- 对固件或多样本工程（dropper+载荷）做本地 Ghidra 反编译调查
- 以 /ask 问答模式核验已有报告中的论断或构造配置解密器

## 场景标签

`网络安全` `Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L5:  An open source agent harness for reverse engineering. Plug in any model, point it at a binary, and it works through
> L7: BINNY is the harness, not the model. It brings the tools (decompiled functions, strings, imports, data, a sealed san

## 星数曲线

```mermaid
xychart-beta
    title "openbin-ai/binny 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 138 --> 183
    line [141, 176, 180]
```

2026-10-18 141 → 2026-10-22 180（+39）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `9b7d7971c584` · [字段定义](../../DATASET.md)*
