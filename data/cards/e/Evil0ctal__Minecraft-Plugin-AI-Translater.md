# Evil0ctal/Minecraft-Plugin-AI-Translater

⭐ 25 · Python · Apache-2.0 · 推送 2026-05-20 · [GitHub](https://github.com/Evil0ctal/Minecraft-Plugin-AI-Translater) · 个人维护 · 中文 README

**将 Minecraft 插件 yml 配置批量翻译成多语言的 Python 脚本**

面向 Minecraft Java 服务器插件服主/管理员的命令行脚本：读取 Input_Files 文件夹中的 yml 配置，调用 OpenAI ChatGPT 3.5 模型翻译为指定语言（默认英文→简体中文，可在 main.py 中改），输出到 Output_Files。内置中英文两套提示词，用自述的 PKVPM 算法拆分合并大型 yaml，支持批量处理与保留关键字；默认最大 Token 为 10240。运行需 Python 3.6+ 并自行配置 OpenAI API 密钥，README 提示翻译结果可能需手动审核。

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

- 调用 ChatGPT 3.5 翻译插件 yml 配置并保留关键字
- PKVPM 算法拆分合并大型 yaml 文件
- 批量处理多个配置文件
- 内置中/英文提示词，可自定义输出语言

## 适用场景

- 把英文插件配置翻译成中文供国内玩家使用
- 批量翻译多个插件的 yml 配置文件
- 处理超长配置文件并保持键与关键字不变

## 场景标签

 · 领域:游戏服务器工具/翻译

## 证据(README 行号)

> L7: 这个工具能够帮助您将Minecraft Java服务器插件的配置yml文件翻译成不同的语言。它基于OpenAI的ChatGPT 3.5模型，并内置了中文和英文两套提示词，开箱即用，准确率高达99%。此外，它还支持大型文件的拆分与合并
> L11: - **高准确率翻译**：基于OpenAI ChatGPT 3.5模型，准确率达99%。

## 星数曲线

```mermaid
xychart-beta
    title "Evil0ctal/Minecraft-Plugin-AI-Translater 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-29 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `51de622603cc` · [字段定义](../../DATASET.md)*
