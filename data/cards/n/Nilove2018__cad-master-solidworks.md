# Nilove2018/cad-master-solidworks

⭐ 4 · C# · GPL-3.0 · 推送 2026-11-01 · [GitHub](https://github.com/Nilove2018/cad-master-solidworks) · [官网](https://github.com/Nilove2018/solidworks-api-skill) · 个人维护

**SOLIDWORKS 插件：内嵌 Claude Code，用自然语言生成并校验 CAD 模型**

SOLIDWORKS 加载项（C#/.NET 4.8），在任务窗格中运行官方 Claude Code。用户描述零件或投放图片，Claude 先研究模型并给出编号计划，用户批准后逐步建模并通过截图、重建检查等本地 MCP 工具逐步验证。遵循开源 solidworks-api skill 的 API 规则，支持拖放 STEP/IGES/STL/PDF、/cad:* 工作流命令、Tasks 检查清单与会话历史。当前为 pre-release，无安装器，需从源码构建并注册；要求 SOLIDWORKS 2025、Windows 10/11 与用户自有 Claude 账号。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- 计划先行：Claude 研究模型并给出编号计划，用户可选全部批准/逐次确认/继续规划
- 本地 MCP 服务器提供视口截图、重建检查、质量属性等 SOLIDWORKS 工具（仅 localhost，会话级 token）
- 遵循开源 solidworks-api skill 的已验证 API 规则，生成参数化零件、装配体与标注图纸
- Tasks 标签页将批准计划变为实时勾选清单，每步构建并验证

## 适用场景

- 用一句描述（如带螺纹盖的水瓶）让 Claude 在 SOLIDWORKS 中建模出图
- 投放照片或 STEP/IGES/STL 文件生成对应模型
- 对现有模型进行审查、检查与 STEP/STL 导出

## 场景标签

 · 领域:工业软件/CAD 自动化

## 证据(README 行号)

> L13: CAD Master is a SOLIDWORKS add-in that runs the official **Claude Code** in a task pane next to your model. You tal
> L17: > **Status: pre-release.** It works and is in daily use, but there is no installer yet. You build it from source (b

## 星数曲线

```mermaid
xychart-beta
    title "Nilove2018/cad-master-solidworks 星数(近 3 点)"
    x-axis ["2026-11-11", "2026-11-20", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-11 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `8021bd30fab1` · [字段定义](../../DATASET.md)*
