# haloshin/ip-diagram-creator

⭐ 262 · MIT · 推送 2026-06-26 · [GitHub](https://github.com/haloshin/ip-diagram-creator) · 个人维护 · 中文 README

**面向个人 IP 创作者的 Agent 技能：把形象与内容生成为图解**

以 SKILL.md 为核心的 Agent Skill 包：读取用户授权照片、主页截图或简介，先固化三张可复用的角色资产（主锚图、规范图、动作扩展图），再把文章、课程、脚本拆成长文配图、知识卡、手绘插图、手机海报或整套 PPT 演讲页面。在无生图能力的环境下输出可复制到 GPT Image 2 等工具的完整 prompt 与返修 prompt。通过 npx skills add 安装，也可手动放入 Agent Skills 目录使用；不适用于高拟真写真与未授权素材。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 先角色建档、再内容拆解、最后生成图解的三段工作流
- 7 类产出：角色三件套、知识卡、Agent 协作图解、PPT 导演规划等
- 无生图环境时输出完整图像生成 prompt 与返修 prompt，不假装已出图
- 支持通过 references/ 目录自定义视觉规则、尺寸模式与 prompt 模板

## 适用场景

- 把我的形象固化成可长期复用的手绘角色资产
- 给文章或课程配一套知识卡和长文插图
- 为直播分享或课件生成整套 PPT 演讲页面

## 场景标签

`图像生成` `提示工程` · 领域:Agent 开发

## 证据(README 行号)

> L7: 它不是单纯的头像生成器，而是 **IP 主角 + 执行 Agent 的知识图解系统**：用户 IP 负责主讲、拆解、批注和调度，执行 Agent 负责搬卡片、递交结果、标记风险、反馈和试错。

## 星数曲线

```mermaid
xychart-beta
    title "haloshin/ip-diagram-creator 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-22"]
    y-axis "stars" 261 --> 263
    line [262, 262]
```

2026-10-18 262 → 2026-10-22 262（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `26aca197eafb` · [字段定义](../../DATASET.md)*
