# EC-DIGIT-CSIRC/openai-cti-summarizer

⭐ 59 · Python · EUPL-1.2 · 推送 2026-08-03 · [GitHub](https://github.com/EC-DIGIT-CSIRC/openai-cti-summarizer) · 组织维护

**将网络威胁情报报告摘要为结构化 schema 的 FastAPI 服务**

欧盟委员会 DIGIT-CSIRC 维护的 FastAPI 服务与 Web 前端：接受 URL、粘贴文本或上传 PDF 形式的 CTI 报告，提取文本后发送至配置的 LLM 提供商（README 标题指向 OpenAI GPT-3.5/GPT-4 API），将输出校验为 CTISummary 结构化 schema，以 JSON 或 Markdown 返回。支持 Docker Compose 部署（文档示例搭配 Traefik 反向代理），本地开发用 uv 管理。采用 EUPL 1.2 许可证。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | EUPL-1.2 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 URL / 粘贴文本 / PDF 上传三种 CTI 报告输入方式
- LLM 输出经 CTISummary schema 校验后返回 JSON 或 Markdown
- 提供用户/管理员/开发者文档与 Docker Compose 部署方式

## 适用场景

- 安全分析师生成 CTI 报告的结构化摘要
- 将多来源威胁情报报告统一为可校验的 JSON schema
- 团队通过 Docker Compose 自托管部署摘要服务

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: FastAPI service and simple web frontend for summarizing Cyber Threat Intelligence (CTI) reports into a validated str
> L11: The report text is extracted, converted where needed, sent to a configured LLM provider, validated as `CTISummary`,

## 星数曲线

```mermaid
xychart-beta
    title "EC-DIGIT-CSIRC/openai-cti-summarizer 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 58 --> 60
    line [59, 59]
```

2026-10-18 59 → 2026-10-27 59（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `82e42b3b502b` · [字段定义](../../DATASET.md)*
