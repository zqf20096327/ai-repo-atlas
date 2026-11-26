# beskvladimir-create/pii-roundtrip

⭐ 3 · Python · Apache-2.0 · 推送 2026-11-10 · [GitHub](https://github.com/beskvladimir-create/pii-roundtrip) · [官网](https://pii-roundtrip.besk.tech) · 个人维护

**本地可逆匿名化俄/英文文档，供外部 LLM 使用**

在本地对俄语与英式英语文档做可逆 PII 匿名化：检测个人数据并替换为一致占位符（如 [PERSON_1]），映射存入 AES-256-GCM 加密 vault，模型回答返回后在本地还原真实值；支持整文档一致性（含俄语格变化）与会话延续。提供 macOS/Windows 离线桌面安装包（内置模型）与命令行、Python 库接口。另含一份可复现基准，对比 pii-guard、Presidio、GLiNER Guard Omni 等既有工具在泄漏率、召回与还原率上的表现。俄语人名占位符还原未达 99% 阈值（README 自述 94.6%）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 检测→占位符替换→加密 vault→本地还原的完整往返流程
- 整文档与会话级占位符一致性，含俄语变格与大小写处理
- 桌面应用内置模型，首次启动即离线运行
- 附带可复现基准：对比 6 个既有 PII 工具的泄漏与还原指标

## 适用场景

- 把含个人数据的合同/病历/HR 文件发给外部 LLM 前做匿名化
- 多轮对话中持续对同一批人物与编号保持占位符一致
- 复现或扩展 PII 匿名化工具的独立基准评测
- 命令行批量处理俄语/英语文本的匿名化与还原

## 场景标签

`模型评测` `文档解析` · 领域:评测与运维

## 证据(README 行号)

> L7: pii-roundtrip replaces personal data in a document with consistent placeholders such as `[PERSON_1]` or `[NHS_1]`, k
> L75: For people who do not use the command line: drop in a Word file, a PDF or text, send the cleaned version to any AI 
> L135: - **Detection.** pii-guard (rules with checksums and ruBERT) for Russian, GLiNER Guard Omni for both languages, pl


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `e45e25026024` · [字段定义](../../DATASET.md)*
