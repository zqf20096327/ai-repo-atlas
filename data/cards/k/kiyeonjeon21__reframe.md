# kiyeonjeon21/reframe

⭐ 24 · TypeScript · NOASSERTION · 推送 2026-09-05 · [GitHub](https://github.com/kiyeonjeon21/reframe) · [官网](https://docs.reframe-video.com) · 个人维护

**声明式动效视频引擎：AI 写场景、人工微调可存活于再生成**

以纯数据场景（TypeScript 场景文件编译为 JSON IR）驱动的确定性视频渲染引擎，输出 mp4。设计循环为：AI 依据内置 guide 写场景，人工在预览中通过 overlay 编辑；AI 重新生成基础场景时，overlay 按稳定节点 id 重新套用，声明实测 100% 保留。提供命名动效预设、矢量设备模型框架、程序化音效、CSV/JSON 批量渲染与 lint 双编译校验确定性。附带 Claude Code 技能插件，可对话生成视频。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 人工编辑以 overlay 形式存活于 AI 场景再生成（实测 100% 保留，孤儿节点显式报告）
- evaluate(scene, t) 纯时间函数，无时钟/无未播种随机，lint 双编译强制确定性
- 命名动效预设（种子化生成器）与 path/motionPath 矢量图元
- CSV/JSON 批量渲染：每行数据成为 overlay，并行输出多视频

## 适用场景

- 用 AI 生成动效视频后继续手动微调颜色、时序而不丢改动
- 从数据表批量生成个性化版本（如团队成员片头）
- 把品牌 SVG 一行命令转为动画 sting
- 在 Claude Code 中对话式描述并生成视频

## 场景标签

`视频生成` · 领域:内容生成

## 证据(README 行号)

> L7: **Declarative motion graphics that AI can write, humans can tweak, and the
> L32: scene.ts  ──(written by you, or by an AI given `pnpm reframe guide`)──▶  IR (plain JSON data)
> L130: No clone needed. `reframe-video` is on npm:

## 星数曲线

```mermaid
xychart-beta
    title "kiyeonjeon21/reframe 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 23 --> 25
    line [24, 24]
```

2026-10-18 24 → 2026-10-27 24（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `59055b65f317` · [字段定义](../../DATASET.md)*
