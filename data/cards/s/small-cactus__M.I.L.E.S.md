# small-cactus/M.I.L.E.S

⭐ 234 · Python · MIT · 推送 2026-07-26 · [GitHub](https://github.com/small-cactus/M.I.L.E.S) · [官网](https://github.com/small-cactus/M.I.L.E.S) · 个人维护

**GPT-4 Turbo 驱动的桌面语音助手，控制家居/Spotify并记忆**

面向个人用户的 macOS/Windows 桌面语音助手：基于 GPT-4 Turbo/GPT-3.5 Turbo 处理自然语言对话，支持基于 5 万样本训练的 Miles 唤醒词、OpenAI TTS 语音合成、网络搜索、天气查询、LaTeX 计算器、摄像头图像识别与本地持久记忆。集成 Home Assistant 控制灯光开关，语音操控 Spotify（需 Premium）。语音唤醒词、图像与音频处理在本地进行，对话数据发送 OpenAI API。用户需自备 API key，OpenAI 部分需付费；作者声明活跃开发已暂停，接收费定制服务。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 唤醒词检测（5 万样本训练）与 OpenAI TTS 语音输出
- Home Assistant 智能家居与 Spotify 语音控制集成
- 本地持久记忆与最多 3 项工具并发处理
- 插件机制：按 docstring 格式编写 Python 函数即可加入工具列表

## 适用场景

- 用自然语言语音操控电脑、音乐与智能灯开关
- 让助手记住日期与个人信息供日后调用
- 语音查询天气、上网搜索与实时计算

## 场景标签

 · 领域:桌面语音助手

## 证据(README 行号)

> L1: # **Miles - GPT 4 Turbo powered voice assistant**
> L27: - 🎤 **Realistic Voice**: Powered by OpenAI's Text-to-Speech technology, Miles has a natural, human-like voice that 

## 星数曲线

```mermaid
xychart-beta
    title "small-cactus/M.I.L.E.S 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 232 --> 235
    line [234, 233, 233]
```

2026-10-18 234 → 2026-10-22 233（-1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `4feb42ff215f` · [字段定义](../../DATASET.md)*
