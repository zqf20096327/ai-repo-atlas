# magicmadeint/wipedown

⭐ 15 · Python · MIT · 推送 2026-06-02 · [GitHub](https://github.com/magicmadeint/wipedown) · [官网](https://magicmadeintelligence.com) · 个人维护

**拦截网页提示注入的本地安全代理，供编码 Agent 使用**

面向 AI 编码 Agent（Hermes、Qwen Code、Cursor、Claude Code 等）的安全代理防火墙：抓取网页内容后剥离恶意格式操纵块、检测已知注入签名，并通过本地 LLM 流将命令式注入语句改写为被动文档化上下文。提供 Python 类编程接口（结构化输出契约）、本地 HTTP 代理模式与 CLI，引擎无关，可对接任意 OpenAI 兼容端点（llama.cpp/Ollama/云服务）。README 声明不保证拦截全部对抗载荷，要求人工在环验证，禁止 auto-approve 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多阶段净化管线：结构剥离+签名检测+LLM 语义中和
- 本地 HTTP 代理模式供 Agent 的 web fetch 工具统一走检
- 引擎无关，任意 OpenAI 兼容端点（llama.cpp/Ollama/OpenAI/Groq）
- wipedown configure --auto 自动发现本地推理环境并生成 .env

## 适用场景

- 为自主编码 Agent 的网页抓取通道加防提示注入代理
- 把净化后的结构化内容安全写入知识库或 agent 记忆
- 本地 LLM 离线净化网页内容供终端使用

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: Prevents prompt injections from web pages & tweets **before** they reach your local coding agent (Hermes, Qwen Code,
> L5: WipeDown acts as an automated security proxy firewall. It fetches messy web content, strips malicious formatting man

## 星数曲线

```mermaid
xychart-beta
    title "magicmadeint/wipedown 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 14 --> 16
    line [15, 15]
```

2026-10-18 15 → 2026-10-30 15（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `e52ef0f56ed9` · [字段定义](../../DATASET.md)*
