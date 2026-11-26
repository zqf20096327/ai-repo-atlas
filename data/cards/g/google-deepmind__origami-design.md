# google-deepmind/origami-design

⭐ 10 · Python · Apache-2.0 · 推送 2026-11-23 · [GitHub](https://github.com/google-deepmind/origami-design) · 组织维护

**把 3D 树状骨架转为可平折折纸折痕图与 3D 模型的 Python 管线**

COrigami 论文的配套 Python 库与 CLI：将度量 3D 树骨架经 prepare/pack/solve/shape 等阶段转换为盒式折叠（box-pleating）折痕图案与带阴影 3D 造型，并用移植的 Flat-Folder 做全局平折可行性验证。提供 47 个内置骨架示例、2D/3D 可视化输出、JSON 序列化、19 工具造型工具箱，并在 .agents/ 下附带 5 个供编码 agent 使用的技能文件。需 Python 3.14+，另附浏览器端 Studio 静态站点展示预计算模型。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 从 StickFigure 到折痕图再到 3D 造型的分阶段不可变管线与一键 bp.fold()
- 全局平折可行性独立验证（Flat-Folder 移植）
- 47 个内置示例骨架与 2,676 棵树的基准评测
- .agents/ 下捆绑 5 个 AI agent 设计技能与端到端 designer agent

## 适用场景

- 把树状骨架 JSON 自动折算为可平折的折痕图案
- 为折纸设计研究做基准与可折性验证
- 在编码 agent 中加载捆绑技能辅助折纸造型迭代

## 场景标签

 · 领域:计算折纸/科研工具

## 证据(README 行号)

> L51: `bp_pipeline` (`bp`) is a standalone Python library and CLI accompanying the
> L81: 6. **3D Origami Shaping, Pose Recipes & Bundled Agent Design Skills**:
> L87:  (`bp.build_folded_mesh_3d()`), and portable AI agent skills under


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 mid · 依据 README sha `57b40ae7f66c` · [字段定义](../../DATASET.md)*
