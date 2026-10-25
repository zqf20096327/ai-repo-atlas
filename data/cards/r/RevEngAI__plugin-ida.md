# RevEngAI/plugin-ida

⭐ 163 · Python · GPL-3.0 · 推送 2026-10-20 · [GitHub](https://github.com/RevEngAI/plugin-ida) · [官网](https://reveng.ai) · 组织维护

**逆向工程师用的 IDA Pro 插件：云端 AI 二进制分析与函数命名**

RevEng.AI 官方开源的 IDA Pro 插件，将当前打开的二进制上传至 RevEng.AI 云端 API 进行分析，基于二进制代码相似性从其符号与函数数据库恢复 strip 后二进制的函数名。功能包括自动批量重命名（按置信度阈值）、单函数/全量函数匹配、AI 反编译并附自然语言解释，以及实验性 Agent Chat（对话式反编译、重命名与跳转导航）。需在 IDA 内配置 API Key，依赖 PyQt5，支持 IDA 8.5–9.2 与 Python 3.10–3.14，从 Releases 下载构建包手动安装。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 上传二进制做云端二进制代码相似性分析
- Auto Unstrip 自动恢复被 strip 的函数名
- AI 反编译并附自然语言解释
- 实验性 Agent Chat：对话式反编译、重命名与跳转

## 适用场景

- 逆向 stripped 二进制时恢复函数名
- 查找与已知函数相似的函数并批量重命名
- 让 AI 生成反编译结果并解释函数行为

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L11: The RevEng.AI IDA plugins allows you to interact with our API from within IDA.
> L22: * AI Decompilation of selected functions
> L131: The `AI Decompilation` tool allows you to get AI generated decompilation of selected functions. You can access it 

## 星数曲线

```mermaid
xychart-beta
    title "RevEngAI/plugin-ida 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 162 --> 164
    line [163, 163]
```

2026-10-18 163 → 2026-10-25 163（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `27e2acf1bc6f` · [字段定义](../../DATASET.md)*
