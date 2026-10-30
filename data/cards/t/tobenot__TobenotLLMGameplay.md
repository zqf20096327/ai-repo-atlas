# tobenot/TobenotLLMGameplay

⭐ 18 · C++ · MIT · 推送 2026-08-27 · [GitHub](https://github.com/tobenot/TobenotLLMGameplay) · 个人维护 · 中文 README

**虚幻引擎 C++ 的 LLM 游戏逻辑插件（“UE 版 Langchain”）**

面向 Unreal Engine 5.3 C++ 开发者的 LLM 游戏插件集合，提供人物系统（喊话/多人会话/一对一聊天组件，含长期记忆自动压缩）、事件系统（动态事件生成、网状叙事触发）、GUID 存档、AI 生图模块与改进的 OpenAI-Api-Unreal GPT 插件（原生 C++、HTTP 中途取消、词嵌入接口）。网状叙事机制：用 LLM 将事件拆成标签组并做词嵌入，按相似度大于 65% 与顺序匹配触发新事件。安装需下载仓库放入 Plugins 文件夹并以 C++ 编译项目。README 顶部声明暂停维护（对应 UE 5.3），仓库保留但无持续更新。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 喊话/Dialogue/Chat 对话组件，含长期记忆自动压缩与历史保存恢复
- 网状叙事：LLM 拆解事件为标签组、词嵌入后按 65% 相似度匹配触发新事件
- 改进 OpenAI-Api-Unreal：原生 C++ 支持、HTTP 中途取消、词嵌入接口
- GUID 存档系统与 AI 生图模块

## 适用场景

- 在 UE5 游戏中快速搭建 LLM 驱动的角色对话与多人会话
- 构建记录事件并据此触发新剧情的网状叙事玩法
- 为游戏角色做带长期记忆的一对一聊天

## 场景标签

`Agent 框架` `Agent 记忆` `图像生成` · 领域:Agent 开发

## 证据(README 行号)

> L14: TobenotLLMGameplay: Tobenot's LLM Game Plugin —— "Langchain" for Unreal Engine C++
> L16: This is a dedicated LLM game plugin for Unreal Engine C++. Perhaps with this plugin, one could quickly establish th
> L111: 虚幻引擎中的"Langchain"！这是一个专用于Unreal Engine C++的LLM游戏插件。也许用这个插件能快速地建立起大模型游戏的相关逻辑~

## 星数曲线

```mermaid
xychart-beta
    title "tobenot/TobenotLLMGameplay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `6273eb493376` · [字段定义](../../DATASET.md)*
