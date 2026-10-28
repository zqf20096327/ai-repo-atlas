# toxy4ny/piedpiper

⭐ 35 · Python · MIT · 推送 2025-11-06 · [GitHub](https://github.com/toxy4ny/piedpiper) · 个人维护

**面向 AI 聊天平台数据暴露的 OSINT 搜索审计工具**

面向安全研究者的 Python 命令行 OSINT 工具：通过搜索引擎 dork 查询（50+ 精制查询）发现 Character.AI、ChatGPT、Claude、Perplexity 等 6 个 AI 聊天平台公开分享链接中可能泄露的敏感信息（API key、邮箱、私人对话等），并用内容校验器做误报过滤（宣称 v3.0 约 5% 误报）与置信度评分，输出风险报告。README 强调仅限教育与授权安全研究，采用 MIT 附加伦理使用条款（商业使用需许可），并记录了对平台的负责任披露流程。需 Python 3.8+，从源码安装运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 针对 6 个 AI 聊天平台的精准 dork 查询引擎
- 内容校验器做平台响应模式识别、置信度评分与误报过滤
- 生成含风险等级与置信度的扫描报告
- MIT 附加伦理使用条款，仅限教育/授权研究，商业使用需许可

## 适用场景

- 对授权范围内的 AI 平台公开链接做数据暴露排查
- Bug Bounty 与合规审计中的自动化侦察
- 网络安全课程中演示 OSINT 与负责任披露流程

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L8: A precision-focused OSINT tool designed for ethical security research of AI conversational platforms. This tool help
> L25: - Character.AI (beta.character.ai)
> L67: 2. **AI Content Validator**

## 星数曲线

```mermaid
xychart-beta
    title "toxy4ny/piedpiper 星数(近 2 点)"
    x-axis ["2026-10-19", "2026-10-28"]
    y-axis "stars" 34 --> 36
    line [35, 35]
```

2026-10-19 35 → 2026-10-28 35（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `3ab946dea1e3` · [字段定义](../../DATASET.md)*
