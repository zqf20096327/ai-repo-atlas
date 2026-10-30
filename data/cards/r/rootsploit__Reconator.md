# rootsploit/Reconator

⭐ 23 · Go · NOASSERTION · 推送 2026-05-04 · [GitHub](https://github.com/rootsploit/Reconator) · 组织维护

**面向赏金与安全测试的 AI 辅助侦察框架（Go 单二进制）**

用 Go 编写的攻击面侦察工具，覆盖子域名枚举、DNS/端口扫描、Web 爬取、WAF/CDN 识别、子域名接管检测、密钥扫描、S3/GCS/Azure 存储测试、GraphQL 检测与截图等模块。AI 层提供多提供商分析（Ollama/Minimax/Kimi/Groq/DeepSeek/Claude/OpenAI/Gemini）与密钥轮换、0-100 风险评分、CVEMap 映射、Graph-of-Thought 攻击路径预测，并以 MCP server/JSON 输出接入 LLM agent。支持 SSH 分布式扫描与 AWS API Gateway IP 轮换；Linux/macOS 完整支持，Windows 需 WSL。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多提供商 AI 分析与 API key 自动轮换
- Graph-of-Thought 攻击路径预测与交互式图可视化
- 内置 MCP server、JSON 进度流与 watch 模式供 AI agent 调用
- 分布式 SSH 扫描与基于 AWS API Gateway 的 IP 轮换

## 适用场景

- 对目标域名做全流程攻击面侦察与报告
- 让 LLM agent 通过 MCP/JSON 输出驱动自动化安全工作流
- 多机分布式大规模扫描并轮换出口 IP

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L20: AI-powered reconnaissance framework for bug bounty hunters and security professionals. Features AI-guided analysis,
> L22: - 🧠 **AI-Powered Analysis** - Multi-provider AI (Ollama/Minimax/Kimi/Groq/DeepSeek/Claude/OpenAI/Gemini) with auto 
> L324: - **🤖 Native MCP Server**: Run Reconator as MCP server for AI agent integration

## 星数曲线

```mermaid
xychart-beta
    title "rootsploit/Reconator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-30 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `994392c9f500` · [字段定义](../../DATASET.md)*
