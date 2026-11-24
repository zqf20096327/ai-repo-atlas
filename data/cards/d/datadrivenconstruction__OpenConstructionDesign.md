# datadrivenconstruction/OpenConstructionDesign

⭐ 6 · Rust · AGPL-3.0 · 推送 2026-11-24 · [GitHub](https://github.com/datadrivenconstruction/OpenConstructionDesign) · [官网](https://openconstructiondesign.com) · 组织维护

**建筑行业用户的 AI 驱动开源 CAD-BIM 编辑器**

用 Rust 编写的 CAD-BIM 编辑器，自带几何内核与文件读取器，提供建模、结构、MEP、图纸、IFC/DWG 读写等完整编辑功能。AI 部分：内置聊天界面通过自然语言描述生成墙体、房间、门窗、管线等草稿，以高亮预览呈现，按 Apply 后才写入模型；支持 MCP 接入外部客户端，JSON brief 可经 ddc CLI 整楼生成，Lua 脚本可参数化造型。模型存储为单个 SQLite 文件，可离线运行；另提供与同团队 OpenConstructionERP 的工程量与估价联动。Windows/Linux 有预编译包，macOS 需从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- AI 草稿以预览呈现，按 Apply 才生效，整个方案为一步撤销
- 内置聊天/ MCP/ JSON brief 三种 AI 驱动方式，支持 Ollama 本地模型免 key 运行
- IFC 2X3/4/4.3 双向读写，另读 DWG/DXF，导出 glTF/STEP/STL/OBJ/3MF/BCF
- 24 个 Lua 参数化造型脚本随编辑器分发，ddc CLI 支持无头批处理

## 适用场景

- 用自然语言描述让 AI 生成或修改建筑模型草稿
- 读取/导出 IFC 文件并做碰撞与规则检查
- 编写 JSON brief 或 Lua 脚本批量生成整楼、体育场等模型
- 将模型工程量发布到 OpenConstructionERP 生成估价

## 场景标签

 · 领域:建筑工程/CAD-BIM

## 证据(README 行号)

> L5:  A free, open-source CAD-BIM editor that your AI can drive.
> L61: readers. You describe a building in the built-in chat, over MCP or as a JSON brief; the editor
> L63: nothing changes in your model until you press **Apply**. Bring a cloud model with your own key,


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `8e2d52a5776a` · [字段定义](../../DATASET.md)*
