# KKingZero/Zypheron-CLI

⭐ 177 · Python · NOASSERTION · 推送 2026-10-01 · [GitHub](https://github.com/KKingZero/Zypheron-CLI) · [官网](https://zypheron.net/cli) · 个人维护

**面向授权测试的本地优先安全 CLI，集成 AI 辅助侦察与扫描**

Go 编写的命令行安全测试工具（v2.0.0 OSS RC），覆盖 scan/recon/osint/fuzz 等 30 余个子命令，scan 封装 nmap/masscan/nikto/nuclei 等外部扫描器。附带可选 Python AI 运行时，支持 Claude、OpenAI、Gemini、DeepSeek、Grok、Kimi、Ollama 等模型提供方，用于聊天、扫描分析与侦察规划（recon 可用 --no-ai 跳过）。AD 与 exploit 步骤需操作员批准，exploit 默认 safe-mode。会话与产出存于 ~/.zypheron。仅限授权测试使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- Go CLI + 可选 Python AI 运行时，支持 7 家模型提供方（含本地 Ollama）
- scan 封装 nmap/masscan/nikto/nuclei，recon 可 AI 规划
- exploit 默认 safe-mode，AD 与利用步骤需操作员批准
- 提供 TUI、FastAPI 可选服务与 .deb/.rpm 发布物

## 适用场景

- 授权渗透测试中做侦察、扫描与信息收集
- 在 DevSecOps 流水线中运行自动化安全测试
- 借助 AI 分析扫描结果并规划测试路径

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: A local-first security CLI for **authorized** work: recon, scanning, and AI-assisted operator workflows.
> L39: Python 3.9+. Chat, scan analysis, recon planning. Providers: Claude, OpenAI, Gemini, DeepSeek, Grok, Kimi, Ollama.
> L91: `scan` wraps nmap / masscan / nikto / nuclei. `recon` can plan with AI (`--no-ai` to skip).

## 星数曲线

```mermaid
xychart-beta
    title "KKingZero/Zypheron-CLI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-22", "2026-10-24"]
    y-axis "stars" 175 --> 178
    line [176, 177, 177]
```

2026-10-18 176 → 2026-10-24 177（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `65204621f00f` · [字段定义](../../DATASET.md)*
