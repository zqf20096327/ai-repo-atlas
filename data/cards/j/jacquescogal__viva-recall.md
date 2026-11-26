# jacquescogal/viva-recall

⭐ 3 · TypeScript · MIT · 推送 2026-11-25 · [GitHub](https://github.com/jacquescogal/viva-recall) · 个人维护

**桌面自主记忆闪卡应用：用 Decision 模型判分开放回答**

Viva Recall 是一款 Electron 桌面应用，面向开放式回忆的闪卡学习。用户写下问题与期望答案，LLM 将答案转成小型 yes/no 检查项；复习时决策模型（Jev）以校准概率逐项作答，代码按规则合成判定，FSRS 安排复习。对判定有异议时可与申诉代理对话，检查项修改须通过回归库校验。支持 Anki/CSV 导入、本地 SQLite 存储、API key 加密保存。依赖 Node 20+ 与 TypeSafe API key，macOS（Apple Silicon）测试通过。

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

- 决策模型 Jev 每次复习单请求输出校准概率，代码确定性合成判定
- 申诉代理以 7 种结果处置争议，检查项编辑须保持回归库原有判定
- 支持 Anki/CSV 导入（手动评分或生成检查项）与 CSV 导出
- API key 经 OS keychain 加密，网络调用均在主进程

## 适用场景

- 用自己的话回答闪卡并由模型判分
- 从 Anki 迁移卡片并生成检查项
- 对判分结果提出申诉并追踪复习进度

## 场景标签

`AI 助手` `知识库管理` · 领域:对话与助手

## 证据(README 行号)

> L5: Viva Recall is a desktop app for open-ended recall. You write a question and the answer you expect. An LLM turns you
> L113:  Architecture: React renderer talks over typed IPC to the Electron main process, which owns keys, the queue, marki
> L123: Requirements: Node 20+, macOS (tested on Apple Silicon), a TypeSafe API key for Jev, and an LLM API key (OpenAI, G


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `38b248ee7e9f` · [字段定义](../../DATASET.md)*
