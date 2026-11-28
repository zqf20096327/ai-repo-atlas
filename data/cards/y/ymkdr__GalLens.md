# ymkdr/GalLens

⭐ 3 · C# · MIT · 推送 2026-11-27 · [GitHub](https://github.com/ymkdr/GalLens) · 个人维护 · 中文 README

**给 Galgame 玩家的 Windows 实时屏幕翻译字幕工具**

运行于 Windows 的视觉小说屏幕翻译工具：截取游戏窗口画面，用系统自带日语 OCR 本地识别台词（约 20~30ms/帧），将文本发往用户自填的 OpenAI 兼容接口做流式翻译，以可点击穿透的字幕层叠加在游戏上。纯外部运行，不注入进程、不读写游戏内存、不修改游戏文件；支持 OCR 失败时的图像兜底、按游戏记忆台词区域与术语表、字幕样式与位置自定义。需 .NET 10 Desktop Runtime 与日语 OCR 语言包，通过源码构建生成单文件 exe 运行。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 OCR（Windows 自带引擎）+ LLM 流式翻译 + 字幕叠加链路
- 纯外部程序：仅截图与叠窗口，不注入、不改游戏文件
- OCR 认不准时自动改用图像输入兜底
- 兼容 OpenAI Chat Completions 规范的任意服务均可接入

## 适用场景

- 玩日文视觉小说时实时看中文字幕
- 接入本地 Ollama/vLLM 服务离线翻译
- 竖排或艺术字文本用手动图像翻译
- 为每个游戏保存台词区域与术语表后重复使用

## 场景标签

`OCR` · 领域:感知与多模态

## 证据(README 行号)

> L3: Windows 上的 Galgame 屏幕实时汉化工具：截取游戏画面 → 本地 OCR 识别日文 → 调用大模型流式翻译 → 在游戏上叠一层中文字幕。
> L14: - **本地 OCR**：用 Windows 自带的 OCR 引擎，20~30 ms 一帧，不联网
> L80: 任何兼容 **OpenAI Chat Completions** 规范（`/chat/completions` + `stream: true`）的服务都能接入：


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `858979c60688` · [字段定义](../../DATASET.md)*
