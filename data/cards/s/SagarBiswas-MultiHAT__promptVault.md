# SagarBiswas-MultiHAT/promptVault

⭐ 34 · TypeScript · Apache-2.0 · 推送 2026-10-29 · [GitHub](https://github.com/SagarBiswas-MultiHAT/promptVault) · [官网](https://promptvault.multihat.dev/) · 个人维护

**离线优先的加密 AI 提示词个人库，带 AI 助手评分改写**

面向 ChatGPT/Gemini/Claude 等工具用户的提示词管理应用：本地浏览器存储，AES-256-GCM 加密（PBKDF2-SHA-256 六十万次迭代），PIN/口令解锁并提供一次性恢复密钥。内置 AI Librarian 通过 Express 代理后端调用 Gemini（多密钥池）与 Groq 兜底，对提示词打分、改写并建议分类标签，API key 不暴露给浏览器。支持 {{变量}} 模板、全文搜索、使用统计、Supabase 可选云同步，并提供 Chromium 浏览器扩展（Alt+P 快速注入提示词）。React 19 + TypeScript 构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- AES-256-GCM 端侧加密 + PBKDF2(600,000 迭代) + 恢复密钥
- AI Librarian 打分/改写提示词（Gemini 多密钥池 + Groq 兜底，密钥走后端代理）
- {{variable}} 模板：复制时交互式填空
- Chromium 扩展可在 ChatGPT/Claude/DeepSeek 等页面一键注入提示词

## 适用场景

- 集中保存、分类并加密管理我常用的 AI 提示词
- 让 AI 助手评估并改写我的提示词，自动建议标题与标签
- 通过浏览器扩展在聊天页面快速调用已保存的提示词
- 在多设备间同步提示词库（可选云同步）

## 场景标签

`提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L54: PromptVault is a privacy-first, client-encrypted AI prompt workbench and local library built with an offline-first 
> L118: - Rate and improve them using a built-in AI assistant
> L122: Everything is stored directly in your browser. No sign-up required. No ads. No data sharing. You own your vault.

## 星数曲线

```mermaid
xychart-beta
    title "SagarBiswas-MultiHAT/promptVault 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-26", "2026-10-28", "2026-10-30"]
    y-axis "stars" 30 --> 35
    line [31, 32, 34, 34]
```

2026-10-18 31 → 2026-10-30 34（+3）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `a400aeb57a00` · [字段定义](../../DATASET.md)*
