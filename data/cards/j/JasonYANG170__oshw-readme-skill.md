# JasonYANG170/oshw-readme-skill

⭐ 21 · 推送 2026-10-02 · [GitHub](https://github.com/JasonYANG170/oshw-readme-skill) · 个人维护 · 中文 README

**为立创开源硬件项目生成产品级展示页面的 AI Skill**

供 Claude Code、QwenCode 等 AI Agent 加载的技能定义：通过六步工作流（交互问答收集信息、确认原理图/PCB/代码/外壳、创建目录、确定图片、生成 HTML、输出图片清单），自动生成立创开源广场（OSHWHUB）项目展示页面，含 Hero、功能介绍、硬件详解、BOM 清单、3D 外壳等模块。需用户预先准备图片、源码与嘉立创 EDA 导出的 BOM/网表文件。仅生成 body 内容、样式内联，支持深色模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 六步工作流驱动 Agent 生成交互式问答→页面
- 按项目类型自动选择模块（Hero/硬件详解/BOM/3D 外壳/源码介绍等）
- 读取嘉立创 EDA 导出的 BOM 与 .enet 网表生成元器件清单
- 仅输出内联样式的 body 内容，支持 light-dark() 深色模式

## 适用场景

- 为我的开源硬件项目自动生成展示页面
- 按图片清单准备渲染图后快速产出 OSHWLab 项目介绍
- 从源码目录结构自动生成源码介绍模块

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L5: 用于 立创开源广场 (OSHWHUB) 硬件开源项目展示页面生成的 AI Skill。让 AI Agent 自动生成产品级展示页面，包含功能介绍、硬件详解、BOM清单、3D外壳展示等模块。
> L105: Skill 定义了一套工作流，AI Agent 在生成展示页面时会遵循：
> L73: git clone https://github.com/easyeda/oshwhub-readme-skill

## 星数曲线

```mermaid
xychart-beta
    title "JasonYANG170/oshw-readme-skill 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-30 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `d2b23dc1ba61` · [字段定义](../../DATASET.md)*
