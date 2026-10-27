# Kazuhito00/Multimodal-Node-Editor

⭐ 38 · Python · Apache-2.0 · 推送 2026-09-16 · [GitHub](https://github.com/Kazuhito00/Multimodal-Node-Editor) · 个人维护 · 中文 README

**组合图像/音频/文本/LLM 管道的节点编辑器，供开发者实验对比**

基于 ReactFlow 的节点编辑器应用：将 100 余个图像、音频、文本、深度学习节点拖拽连线组成处理管道，支持摄像头/麦克风实时处理、图形 JSON 导入导出、无 GUI 的 headless 执行以及 Google Colaboratory 后端启动。AI 相关节点包括图像分类、目标检测、深度/姿态估计、OCR、语音识别（Google STT/Vosk）及 OpenAI LLM/VLM/STT/图像生成调用。新节点以 TOML + Python 定义，无需自建 GUI。README 注明部分基础处理节点尚有缺失。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 100+ 标准节点覆盖图像/音频/文本/深度学习/数学运算
- 支持 Web 摄像头与麦克风的实时处理
- 图形可 headless 执行，亦可在 Google Colaboratory 上启动
- TOML + Python 定义新节点，含 OpenAI LLM/VLM/STT/图像生成节点

## 适用场景

- 可视化搭建并对比图像/音频处理管道
- 接入 OpenAI LLM/VLM 做多模态实验
- 在 Colab 上无本地环境运行处理图形

## 场景标签

`多模态` `工作流自动化` · 领域:效率与自动化

## 证据(README 行号)

> L4: ノードエディターベースのマルチモーダル処理アプリケーションです。
> L8: - 画像・音声・テキスト・深層学習など、100 以上のノードを標準搭載
> L370: |OpenAI LLM|OpenAI LLM APIを呼び出す Executeボタンを押したタイミングで実行する ※コンフィグの api_keys.openai にOpenAI APIキーを指定している場合のみ有効|

## 星数曲线

```mermaid
xychart-beta
    title "Kazuhito00/Multimodal-Node-Editor 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 37 --> 39
    line [38, 38]
```

2026-10-18 38 → 2026-10-27 38（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9d45c9eafc84` · [字段定义](../../DATASET.md)*
