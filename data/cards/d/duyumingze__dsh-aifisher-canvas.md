# duyumingze/dsh-aifisher-canvas

⭐ 3 · TypeScript · NOASSERTION · 推送 2026-11-22 · [GitHub](https://github.com/duyumingze/dsh-aifisher-canvas) · 个人维护 · 中文 README

**把 AI 创作无限画布做成 DSH 插件，Agent 替你搭建生成流水线**

本仓库是 DeepSeek Harness（DSH）的插件，将上游 AIFISHER 画布源码打补丁后装配为 DSH 侧边栏中的无限画布工作台。DSH 原生 Agent 通过 canvas_control 工具直接操作画布对象：创建节点、连线、填参、整理素材，生成批次需用户在确认卡上授权触发。支持本地 ComfyUI 集成（扫描节点/模型/LoRA、导入自定义工作流）与多条云端生成通道，并含调色合成器、分镜板、项目记忆与视觉一致性锚点。需自备上游 AIFISHER 源码方可构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- DSH 原生 Agent 通过 canvas_control 工具直接建节点、连线、填参
- 本地 ComfyUI 集成：扫描本机节点/模型/LoRA，导入自定义工作流为画布节点
- 多云端生成通道：火山方舟、OpenAI 兼容接口、ModelScope、DashScope 等
- 生成确认卡由用户触发费用授权，生成事件与失败重试推回对话

## 适用场景

- 用自然语言让 Agent 在画布上搭建文生图/文生视频工作流
- 分镜创作中跨镜头锁定角色与画风的一致性
- 本地 ComfyUI 用户把自定义工作流变成可视化画布节点
- 在画布内完成调色、扩图、图层拆分等素材处理

## 场景标签

`工作流自动化` `图像生成` `视频生成` · 领域:效率与自动化

## 证据(README 行号)

> L6: 一块专业级 AI 创作无限画布 —— 你说一句话，DSH 原生 Agent 在画布上替你搭好整条流水线；
> L78: 这不是在插件里套了一个写死提示词的"生图对话框"——你右侧的聊天栏就是完整的 DSH 原生 Agent（模型走 DSH 配置，可接入任意兼容的大模型 API：Base URL + Key）：
> L161: - **DeepSeek Harness** ≥ 0.1.0-rc.7（桌面版 / Web 版都行）

## 星数曲线

```mermaid
xychart-beta
    title "duyumingze/dsh-aifisher-canvas 星数(近 2 点)"
    x-axis ["2026-11-18", "2026-11-26"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-18 3 → 2026-11-26 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `163ac386ae4e` · [字段定义](../../DATASET.md)*
