# z26zheng/CipherTax

⭐ 14 · Python · MIT · 推送 2026-04-29 · [GitHub](https://github.com/z26zheng/CipherTax) · 个人维护

**本地 PII 脱敏层：税务文档安全送 AI 计算与咨询**

面向个人报税场景的本地隐私处理工具：从税务 PDF/照片提取文本（含 OCR），用 Microsoft Presidio 加自建识别器检测 SSN、EIN、姓名、银行账号等 PII，替换为令牌后仅将脱敏文本发送给 Claude，响应在本地还原真实信息；映射表存于 Fernet 加密本地保管库，发送前二次检测并可阻断含 PII 的调用。内置 2024 年联邦税计算引擎与优化建议，声明仅供估算非税务建议。以 pip 包与 CLI 提供。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Presidio + 自建识别器的 PII 检测与确定性令牌化（保留财务金额）
- Fernet/AES-128-CBC + PBKDF2 加密本地保管库，发送前二次 PII 检测阻断
- 五级数据敏感度分级（DSL）驱动脱敏决策，DSL 5 凭据拒绝处理
- 内置 2024 年联邦税计算器与优化建议，159 项测试

## 适用场景

- 把 W-2/1099 等税务文档交给 AI 分析而不泄露 PII
- 让 AI 回答税务资格问题并本地还原结果
- 本地估算联邦税并获得优化建议

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L28: CipherTax is a **local-first privacy layer** that sits between your tax documents and AI. It:
> L34: 5. **Sends** only the sanitized text to Claude
> L190: ## Tax Calculation Engine

## 星数曲线

```mermaid
xychart-beta
    title "z26zheng/CipherTax 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `bbb9849fcfa5` · [字段定义](../../DATASET.md)*
