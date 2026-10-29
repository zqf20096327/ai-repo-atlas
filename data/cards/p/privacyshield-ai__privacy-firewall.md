# privacyshield-ai/privacy-firewall

⭐ 245 · JavaScript · MIT · 推送 2026-01-16 · [GitHub](https://github.com/privacyshield-ai/privacy-firewall) · 个人维护

**浏览器端 AI 防泄漏扩展：拦截发往 AI 聊天工具的敏感数据**

Chrome Manifest V3 扩展，在用户向 ChatGPT、Claude、Gemini 等 AI 聊天站点粘贴或输入文本前进行敏感数据检测：第一层正则规则识别邮箱、电话、信用卡、SSN、API 密钥、JWT、私钥等格式；第二层用 BERT NER 模型（Xenova/bert-base-NER-uncased）经 ONNX Runtime Web/WASM 在浏览器内识别人名、机构、地点。全部处理本地完成，无数据外传，首次运行需下载约 50MB 模型并本地缓存。提供打包下载安装与源码构建（npm + node build.js）两种方式，要求 Chrome 120+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 正则层 + BERT NER AI 层双层检测，均在浏览器本地运行
- 识别邮箱/电话/信用卡/SSN/AWS密钥/JWT/私钥/IP/MAC/地址等 11 类格式化 PII 与 3 类命名实体
- 按站点启用保护，默认覆盖 ChatGPT/Claude/Gemini/Copilot/Poe/Grok/DeepSeek
- 可配置阻断或警告、逐类 PII 开关与 AI 置信度阈值

## 适用场景

- 防止把客户邮件、API 密钥等敏感内容误贴进 AI 聊天工具
- 企业个人使用中对 AI 工具输入做本地 DLP 审查
- 在完全离线/无外传要求的环境下检测 PII

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L41: |🧠 **Local AI Detection**|BERT NER model runs in-browser via ONNX/WASM|
> L57: 1. **Instant Regex Layer** — Catches obvious patterns (emails, credit cards, API keys) in milliseconds

## 星数曲线

```mermaid
xychart-beta
    title "privacyshield-ai/privacy-firewall 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-23", "2026-10-26", "2026-10-29"]
    y-axis "stars" 243 --> 246
    line [245, 244, 245, 245]
```

2026-10-18 245 → 2026-10-29 245（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `8d7e8e4e0da9` · [字段定义](../../DATASET.md)*
