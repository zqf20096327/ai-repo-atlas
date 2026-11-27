# zhoushimiaov/archviz-render-enhancer

⭐ 3 · Python · MIT · 推送 2026-10-22 · [GitHub](https://github.com/zhoushimiaov/archviz-render-enhancer) · 组织维护 · 中文 README

**建筑效果图 AI 增强的 ComfyUI 三管线技能包**

面向建筑/室内效果图画师的 ComfyUI 技能包，提供三条图像增强管线：FLUX2-Klein 语义重绘（换氛围/材质）、NVIDIA DLSS5 离线增强放大（零漂移）、SeedVR2 生成式超分，三条管线可串联使用。包含 3 个 API 工作流 JSON、4 个 Python 脚本（提交/对比/自检/出图）、环境自检与排障文档。要求 NVIDIA RTX 30/40/50 系显卡与特定 PyTorch 版本（2.11.0+cu130），支持局域网多机分布式调度，注明 ComfyUI HTTP 接口无鉴权仅限内网使用。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 三管线覆盖重绘/零漂移增强/生成式超分，按'是否允许改画面'选型
- 含环境自检脚本（GPU/驱动/torch/节点/模型一次性检查）
- 支持局域网多机分布式调度（ComfyUI --listen + queue_workflow.py）
- 热/冷模型分离：低频模型可留机械盘经 extra_model_paths.yaml 挂载

## 适用场景

- 效果图交付前放大发糊、需要超分增强
- 客户要求不改动画面的纯增强放大
- 换白天/黄昏氛围或材质倾向的语义重绘

## 场景标签

`图像生成` `图像视频处理` · 领域:内容生成

## 证据(README 行号)

> L5: > ComfyUI 技能包：建筑与室内效果图的 AI 增强三管线 —— **FLUX2-Klein 语义重绘**、**N卡 DLSS5 图像增强+放大**、**SeedVR2 生成式超分**。
> L41: |显卡|NVIDIA RTX 30/40/50 系|DLSS5 离线运行时需 RTX；实测 4080 16GB / 5070 12GB|

## 星数曲线

```mermaid
xychart-beta
    title "zhoushimiaov/archviz-render-enhancer 星数(近 2 点)"
    x-axis ["2026-11-26", "2026-11-27"]
    y-axis "stars" 2 --> 4
    line [3, 3]
```

2026-11-26 3 → 2026-11-27 3（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `8042b26152f1` · [字段定义](../../DATASET.md)*
