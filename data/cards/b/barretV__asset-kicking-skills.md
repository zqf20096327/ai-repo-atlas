# barretV/asset-kicking-skills

⭐ 3 · Python · MIT · 推送 2026-11-26 · [GitHub](https://github.com/barretV/asset-kicking-skills) · 个人维护

**给编码 agent 用的本地游戏美术技能集：2D/像素/3D/音效生成**

一组供 Claude Code、Codex、Cursor 等可执行命令的编码 agent 安装运行的本地 AI 技能，覆盖彩绘 2D 插画与 UI 部件、真网格像素画（LoRA + Aseprite 逐格编辑）、概念图转 3D 雕塑、SkinTokens 自动绑骨与 Blender 动画、程序化与 Stable Audio 3 音效。核心机制是 forge loop：生成候选、按分数线打分、迭代精修，另有零安装 dashboard 实时查看与提前采纳。全部本地运行，按 GPU 显存分 5 个档位，默认模型均声明允许商用；无模型权重入库，下载需用户批准。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `gpu-8g` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- forge loop：生成→按分数线打分→单点修正→迭代直至达标
- 像素画走真 8×8 网格 LoRA，可在 Aseprite 逐格修补并导出 sprite sheet
- 概念图→TRELLIS.2/Hi3D 3D 雕塑→SkinTokens 自动绑骨→Blender 动画与量化验证
- _setup/detect.py --dry-run_ 免安装预检硬件与档位

## 适用场景

- 让 agent 为独立游戏批量产出风格一致的图标、UI 套件与概念图
- 把旧像素 sprite 升级、做逐帧动画并导出引擎可用的 sprite sheet
- 从概念图生成可绑骨动画的 GLB 模型供 Godot/Unity/Unreal 使用
- 生成并后期处理游戏音效（mono、裁剪、响度匹配、带 manifest）

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L5: Concept art · painted game UI and icons · real pixel art · image to 3D · auto-rigging and animation · sound effects
> L8:  Setup is one sentence to your coding agent:
> L105: your agent ── reads AGENTS.md


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `5eec49a47358` · [字段定义](../../DATASET.md)*
