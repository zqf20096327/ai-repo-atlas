# atharvnaik1/ipaship-audit

⭐ 104 · TypeScript · MIT · 推送 2026-05-25 · [GitHub](https://github.com/atharvnaik1/ipaship-audit) · 个人维护

**iOS 应用提交前的 App Store 合规 AI 审计工具**

面向 iOS 开发者的开源合规审计应用：上传 .ipa 文件（最大 150MB），自动解包提取源文件，交由用户自选的 AI 提供商（Anthropic/OpenAI/Gemini/OpenRouter，BYOK 模式）生成对照 Apple 六大类审核指南的结构化报告，含 pass/fail 标记、严重度与整改建议，可导出 Markdown/PDF，支持流式生成。文件在临时目录处理即删，API key 仅存浏览器。提供 Next.js Web 应用与十余种语言的 CI/CD 包装器。需 Node.js 18+、MongoDB 与 unzip。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 6 大 App Store 审核指南类别的结构化审计报告
- 多提供商 BYOK（Anthropic/OpenAI/Gemini/OpenRouter），key 仅存浏览器
- 临时目录处理文件即删、execFile 防注入、速率限制等安全机制
- 提供 NPM/Python/Rust/Go/Brew 等十余种语言的 CI/CD 包装器

## 适用场景

- iOS 应用提交前自查 App Store 合规风险
- 在 CI/CD 流水线中自动审计 .ipa 构建
- 按严重度与整改计划提前修复合规问题

## 场景标签

`代码审查` · 领域:编码与开发

## 证据(README 行号)

> L3: AI-powered iOS App Store compliance auditor. Upload your `.ipa` file and get a comprehensive audit against Apple's R
> L13: - **Multi-Provider AI** — Bring your own key from Anthropic (Claude), OpenAI (GPT), Google Gemini, or OpenRouter

## 星数曲线

```mermaid
xychart-beta
    title "atharvnaik1/ipaship-audit 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-28"]
    y-axis "stars" 103 --> 109
    line [108, 104, 104]
```

2026-10-18 108 → 2026-10-28 104（-4）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `4e933c230caa` · [字段定义](../../DATASET.md)*
