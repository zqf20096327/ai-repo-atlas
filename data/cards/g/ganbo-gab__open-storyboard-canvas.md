# ganbo-gab/open-storyboard-canvas

⭐ 405 · TypeScript · NOASSERTION · 推送 2026-11-20 · [GitHub](https://github.com/ganbo-gab/open-storyboard-canvas) · [官网](https://ganbo-gab.github.io/open-storyboard-canvas/) · 个人维护 · 中文 README

**面向分镜创作者的本地优先 AI 分镜节点画布桌面应用**

基于 Tauri 2 + React 的本地桌面应用，将多模型渠道接入、无限节点画布、三维导演台与多作用域 Agent 整合到同一工作流。用户通过渠道配置接入图片、视频、音频与文本模型，在生成工作台发起生成，在节点画布编排可复用工作流，并可用三维预演台安排人物走位与机位后回流画布。项目与素材默认保存在本机，API Key 托管于系统钥匙串/凭据管理器。Agent 提供三种执行模式，均不开放任意系统文件或命令。提供 Windows/macOS 安装包，macOS 当前为 ad-hoc 临时签名。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 文本、图片、视频、音频统一生成工作台，提交记录含模型、参数与原任务 ID
- 无限节点画布支持多种节点类型连线编排与非破坏性素材编辑
- 三维导演台支持 GLB/glTF 导入、走位时间轴与四视图拍摄回流
- 多作用域 Agent 支持请求确认/辅助执行/完全执行三种模式

## 适用场景

- 为 AI 短片与漫画创作编排分镜工作流
- 接入多个模型渠道统一管理生成任务
- 用三维预演台安排走位与机位后取景回流画布
- 挂载本地 Markdown 笔记目录作为创作知识库

## 场景标签

`图像生成` `视频生成` `知识库管理` · 领域:内容生成

## 证据(README 行号)

> L5: **Local-first AI Storyboard & Infinite Canvas Desktop App**
> L18: **Open Storyboard Canvas** 是一款本地优先（Local-first）的桌面 AI 分镜（AI Storyboarding）工作台，将多模型渠道、无限节点画布（Infinite Canvas）、三维导演台与
> L20: 面向 AI 短片与漫画创作者，覆盖“快速试模型 → 节点化编排 → 三维走位取景 → 素材复用”，项目与素材默认保存在本机。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `6dd629e5e7e4` · [字段定义](../../DATASET.md)*
