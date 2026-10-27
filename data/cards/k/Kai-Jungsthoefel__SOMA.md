# Kai-Jungsthoefel/SOMA

⭐ 378 · TypeScript · GPL-3.0 · 推送 2026-10-26 · [GitHub](https://github.com/Kai-Jungsthoefel/SOMA) · [官网](https://somacad.app/) · 个人维护 · 中文 README

**让编程 Agent 用 CadQuery 做参数化 3D 建模的桌面应用**

面向创客的 Electron 桌面 CAD 应用：用户用自然语言描述零件，外部 CLI 编程代理（Claude Code、Codex CLI、Gemini CLI 等，需自装自登录）在终端中编写 CadQuery Python 代码，SOMA 每次变更后重建模型并展示 3D 结果；用户可点击测量、在视图上标注后反馈给代理迭代。内置规则/技能集（3D 打印、CNC、钣金、公差）、标准件库、STEP 导入导出、FEM 分析（CalculiX）、历史回放与动画。单个 .soma 文件保存代码、结果与历史。自述为早期原型，主要在 Windows 测试，0.x 版本间文件格式与 soma API 可能变更。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 代理写 CadQuery 代码，SOMA 每次变更重建模型并展示
- 提供 soma build/analyze/render 命令行工具与 AGENTS.md 规则、按模型启用的技能集
- 标准件与 STEP 导入，STEP/STL/3MF/DXF/PDF 图纸导出
- 基于 CalculiX 的 FEM 分析（悬垂、壁厚、强度）与版本历史

## 适用场景

- 快速为项目做出外壳、支架、安装座等零件并导出打印
- 不熟悉 CadQuery 也能通过对话迭代参数化 3D 模型
- 对模型做悬垂、壁厚与强度分析后再导出

## 场景标签

 · 领域:CAD/3D 建模

## 证据(README 行号)

> L9: You tell the agent what you need. It writes the model as Python code with CadQuery, SOMA builds it and shows the res
> L13: A CAD program where the AI does the CAD and you are the designer. SOMA brings together the three parts this needs: 
> L17: SOMA is not an agent of its own. Any CLI agent that can read files and run commands works: Claude Code, OpenCode, C

## 星数曲线

```mermaid
xychart-beta
    title "Kai-Jungsthoefel/SOMA 星数(近 2 点)"
    x-axis ["2026-10-26", "2026-10-27"]
    y-axis "stars" 377 --> 379
    line [378, 378]
```

2026-10-26 378 → 2026-10-27 378（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `d77ef5d18d8e` · [字段定义](../../DATASET.md)*
