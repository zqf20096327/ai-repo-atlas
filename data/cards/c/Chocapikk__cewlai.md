# Chocapikk/cewlai

⭐ 14 · Go · MIT · 推送 2026-10-15 · [GitHub](https://github.com/Chocapikk/cewlai) · 个人维护

**AI 增强的渗透测试字典生成与目标侦察 Go 工具**

用 Go 重写的 CeWL 类工具：爬取 HTTP/FTP/SFTP/SMB/S3 目标，解析 10 余种内容格式，提取词汇、邮箱（含混淆格式）、文档元数据，并用 800+ trufflehog 检测器做密钥扫描、转储文件。AI 部分将爬取摘要发给 LLM（Groq/OpenRouter/Cerebras/HuggingFace/Anthropic/OpenAI 或本地 Ollama/LM Studio/vLLM 及 opencode server），生成站点上不存在但上下文相关的词汇与候选密码，支持 5 种提示模式与自定义 prompt。面向渗透测试与红队人员，单一 Go 二进制分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多协议爬取（HTTP/FTP/SFTP/SMB/S3）与 10+ 内容格式解析
- 7 类 AI provider 或本地模型生成上下文相关词汇与密码
- 800+ trufflehog 检测器的密钥扫描（仅 regex）
- CUPP 式密码变异（leet、反转、后缀、自定义 JSON）

## 适用场景

- 对目标站点生成定制化密码字典
- 扫描网站泄露的 API key 与凭据
- 敏感任务中用本地 Ollama 模型做 AI 增强，数据不出网

## 场景标签

`网页抓取` `网络安全` · 领域:效率与自动化

## 证据(README 行号)

> L8: Replaces CeWL + CUPP in a single Go binary. Crawls HTTP, FTP, SFTP, SMB, and S3 targets, parses 10+ content formats,
> L203: 3. The context is sent to the LLM with a specialized prompt (comma-separated output to save tokens). The tool retr

## 星数曲线

```mermaid
xychart-beta
    title "Chocapikk/cewlai 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-30", "2026-10-31"]
    y-axis "stars" 13 --> 16
    line [15, 14, 14]
```

2026-10-18 15 → 2026-10-31 14（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `c76e440d46b8` · [字段定义](../../DATASET.md)*
