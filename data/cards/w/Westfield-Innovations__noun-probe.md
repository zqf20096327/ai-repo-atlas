# Westfield-Innovations/noun-probe

⭐ 3 · Python · 推送 2026-11-20 · [GitHub](https://github.com/Westfield-Innovations/noun-probe) · [官网](https://azus.ai/tools/noun-probe/) · 组织维护

**从远程读取 Noun Probe 词表的 Python 读取器，供文档分析用**

noun-probe 是 Noun Probe 工具的读取器包：从官方地址 azus.ai 实时读取词表，与用户自己的 AI 模型配合，识别文档中承担多重职责的词。AUDIT 与 VISION 两种模式。仅向官方地址发起只读请求，不发送用户文档，不写磁盘，读取结果内存缓存五分钟，报告末尾附四行署名。仅依赖 Python 3.11+ 标准库，单文件实现；可用 prompt() 不调用 AI 获取文本，read() 可固定编号版次。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 通过 pip 安装，仅需 Python 3.11+ 标准库，单文件
- 从官方地址实时读取词表，支持 read(edition=3) 固定版次
- 不发送用户文档、不写磁盘、只访问官方地址
- 报告自动附四行 credit 署名

## 适用场景

- 审计文档中承担多重语义职责的词
- 将词表接入自定义 AI 调用流程
- 需要不落盘、无遥测的只读分析工具链

## 场景标签

 · 领域:文本/语言分析工具

## 证据(README 行号)

> L3: The Noun Probe finds the words in a document that are doing more than one job. This package is its reader.
> L9: The words of the Noun Probe live only at that address. People read them there. Programs read them there through this
> L17: It needs nothing beyond Python 3.11 or later.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `985282597394` · [字段定义](../../DATASET.md)*
