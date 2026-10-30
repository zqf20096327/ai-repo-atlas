# mirzayasirabdullahbaig07/PromptGuard-AI

⭐ 43 · HTML · 推送 2026-09-14 · [GitHub](https://github.com/mirzayasirabdullahbaig07/PromptGuard-AI) · [官网](https://promptguardai.netlify.app/) · 组织维护

**单文件 AI 提示词安全扫描平台：实时分类提示词威胁**

PromptGuard 是一个纯 HTML/CSS/JS 单文件 Web 应用，实时扫描用户提示词并分类为 SAFE/SUSPICIOUS/DANGEROUS，覆盖提示注入、越狱、数据外泄等 6 类威胁。核心机制为 RAG：将自有安全策略切块并用 nomic-embed-text-v1_5 嵌入为 768 维向量，浏览器内做余弦相似度检索，由 Groq API 上的 llama-3.3-70b-versatile 生成裁定并引用具体策略条款。另提供策略问答聊天与扫描历史。零依赖，浏览器直接打开或部署到 Netlify，需自备 Groq API key。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 实时扫描并输出威胁类型、严重度与置信度，引用具体策略条款
- RAG 策略接地：nomic-embed-text-v1_5 嵌入 768 维向量，浏览器内余弦相似度检索
- 内置 OWASP LLM Top 10、企业 AI 政策、HIPAA 三种策略模板
- 纯 HTML/CSS/JS 单文件，零依赖、无需构建，可部署到 Netlify

## 适用场景

- 上线前检查提示词是否含注入、越狱等攻击
- 按自有安全策略对提示词做合规裁定并留痕
- 通过对话查询组织 AI 治理规则

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L13: **PromptGuard** is a single-file AI security platform that scans user prompts in real-time and classifies them as *
> L23: |🤖 **llama-3.3-70b-versatile**|State-of-the-art LLM analysis running on Groq's ultra-fast inference API|

## 星数曲线

```mermaid
xychart-beta
    title "mirzayasirabdullahbaig07/PromptGuard-AI 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-30"]
    y-axis "stars" 41 --> 44
    line [42, 43, 43]
```

2026-10-18 42 → 2026-10-30 43（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `0d299143e105` · [字段定义](../../DATASET.md)*
