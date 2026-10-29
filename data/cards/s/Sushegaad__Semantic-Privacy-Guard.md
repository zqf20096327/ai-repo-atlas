# Sushegaad/Semantic-Privacy-Guard

⭐ 21 · Java · NOASSERTION · 推送 2026-06-14 · [GitHub](https://github.com/Sushegaad/Semantic-Privacy-Guard) · [官网](https://sushegaad.github.io/Semantic-Privacy-Guard/docs/index.html) · 个人维护

**Java 中间件库：在文本到达 LLM 前检测并脱敏 PII**

面向 Java 开发者的本地 PII 防火墙库：三层混合管线（正则+Naive Bayes ML+Apache OpenNLP NER）识别 SSN、信用卡号、姓名、邮箱等 12 类敏感信息，以 TOKEN/MASK/BLANK 三种模式脱敏，支持 JSON/XML 结构化脱敏与逐行流式处理（堆占用恒定）。零云依赖、进程内运行，提供 Spring AI 适配器与 Spring Boot HTTP Filter 模块，LLM 响应可通过反向映射去标记化。NER 模型需自行下载、OpenNLP 为可选依赖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Regex + Naive Bayes + OpenNLP NER 三层检测，多层命中提升置信度
- 流式处理大文件，堆占用按最长单行（约 4KB）有界
- Spring AI Advisor 与 Spring Boot HTTP Filter 两个集成模块，附带反向映射去标记化
- 自定义模式注册表支持机构专属标识符，全离线运行

## 适用场景

- 在 LLM 网关层拦截员工提示词中的客户 SSN 与邮箱
- 对应用日志与工单做 PII 清洗后再存储或索引
- 医疗/金融管道中脱敏病历号、员工 ID 等领域标识符
- 为满足 GDPR / EU AI Act 构建可审计的输入拦截层

## 场景标签

 · 领域:数据安全/LLM 基础设施

## 证据(README 行号)

> L11: **AI Privacy Firewall for Java.** Detect and redact sensitive data before it reaches ChatGPT, Claude, Gemini, MCP t
> L103: **LLM API gateway** — Intercept every prompt at the gateway layer before it reaches OpenAI, Anthropic, or any thir
> L205: ### Spring AI Integration

## 星数曲线

```mermaid
xychart-beta
    title "Sushegaad/Semantic-Privacy-Guard 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-29 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f910a61f4e18` · [字段定义](../../DATASET.md)*
