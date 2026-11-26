# newmean-ai/pii

⭐ 194 · Python · Apache-2.0 · 推送 2026-11-17 · [GitHub](https://github.com/newmean-ai/pii) · [官网](https://pii.newmean.ai) · 组织维护

**浏览器端多语言 PII 识别与脱敏 SDK，文本不出设备**

在浏览器 WebAssembly 中检测并遮蔽文本中个人信息的 SDK，覆盖姓名、邮箱、电话、地址、证件号等 11 类标签，支持 54 种语言；提供 nano/small/medium/large 四档模型（2.6–15.5 MB），模型文件从 Hugging Face 下载并按 SHA-256 校验。同一套模型通过 C 引擎分发到 Python、iOS、Android、Flutter、Rust 等平台。另支持表格（CSV/TSV）整表脱敏、block/allow 用户词表、可选正则模式层（默认关闭）。许可证允许包括商业在内的任意使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 54 种语言、11 类 PII 标签，四档模型 2.6–15.5 MB
- 浏览器 WebAssembly 端上运行，原文不离开设备
- 表格模式保持分隔符/引号/换行不被遮蔽，输出仍为合法表格
- 同一模型分发到 Python/iOS/Android/Flutter/Rust 多端

## 适用场景

- 在前端对用户输入的文本做 PII 遮蔽后再发送
- 对调研导出的 CSV/TSV 表格进行批量脱敏
- 用 block/allow 词表定制业务字段的遮蔽与保留

## 场景标签

 · 领域:隐私/数据安全工具

## 证据(README 行号)

> L5: **Browser-side PII redaction.** Detect and mask personal information (names, emails, phone numbers, addresses, IDs, 
> L10: - Runs in WebAssembly: the SDK's own built-in engine (default, about 13 KB) or onnxruntime-web


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `0f5f119e77f0` · [字段定义](../../DATASET.md)*
