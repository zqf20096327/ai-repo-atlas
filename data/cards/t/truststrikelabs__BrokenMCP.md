# truststrikelabs/BrokenMCP

⭐ 14 · Python · 推送 2026-08-17 · [GitHub](https://github.com/truststrikelabs/BrokenMCP) · [官网](https://truststrikelabs.com/) · 组织维护

**OWASP MCP Top 10 漏洞靶场：每类风险一个可运行实验环境**

TrustStrike Labs 维护的故意脆弱的 MCP 服务器集合，按 OWASP MCP Top 10 组织为 10 个独立实验（令牌泄露、权限提升、工具投毒、供应链、命令注入、审计缺失、影子服务器等），每个实验位于独立 mcpNN 目录，配套博客 walkthrough。提供 GUI（浏览器 127.0.0.1:8410 选择并启动实验）与 CLI 两种运行方式。README 声明仅供安全学习，禁止公网部署或生产复用其代码。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 10 个实验对应 OWASP MCP Top 10 全部风险类别
- GUI 实验选择器与 CLI 两种启动方式
- 每个实验独立目录，配套博客 walkthrough 文章
- 附带 MCP Hacking 基础教程链接

## 适用场景

- 在安全环境中练习发现和修复 MCP 漏洞
- 学习 OWASP MCP Top 10 各类风险的实际表现
- 安全培训或渗透测试课程的实验环境

## 场景标签

`网络安全` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L3: BrokenMCP is a vulnerable implementation of the Model Context Protocol (MCP) for educational purposes.
> L5: BrokenMCP - deliberately vulnerable MCP servers, one lab per OWASP MCP Top 10 risk

## 星数曲线

```mermaid
xychart-beta
    title "truststrikelabs/BrokenMCP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `acbdf5db0378` · [字段定义](../../DATASET.md)*
