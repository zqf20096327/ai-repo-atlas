# MoJIeAIGC/comfyui-MJAPI-party

⭐ 55 · Python · Apache-2.0 · 推送 2026-09-05 · [GitHub](https://github.com/MoJIeAIGC/comfyui-MJAPI-party) · [官网](http://www.mojieaigc.com) · 组织维护 · 中文 README

**给 ComfyUI 用户的聚合 API 节点包：一个 key 调用多家模型**

摩诘AI开发的 ComfyUI 自定义节点集合，将多家厂商的图像、视频、LLM API（Gemini、NanoBanana、Qwen-image、seedance、seedream、Flux、gpt-image 等）整合为节点，用户在 mojieaigc.com 注册账户获取单一 API-key，配置 config.ini 后即可在 ComfyUI 中以节点方式调用，降低本地算力与部署门槛。需先安装 ComfyUI，可经 comfyui-manager 或 git clone 安装，节点更新在 ComfyUI 设置内完成。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 单一 API-key 统一管理多家模型接口
- 覆盖图像生成/编辑、视频生成、图片翻译、高清放大、自动抠图、服装工作流等节点
- 支持 Gemini3-LLM 节点的结构化输出、web_search、视频与 PDF 读取
- 提供 workflow 目录下的示例工作流与 doc 目录下的节点文档

## 适用场景

- 低配电脑上通过云端 API 运行 ComfyUI 图像/视频生成
- 电商场景做多图详情页、服装模特生成与白底图提取
- 在 ComfyUI 中统一管理多家模型 API 密钥并按节点调用

## 场景标签

`图像生成` `视频生成` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13:  MojieAI开发的Comfyui自定义节点工具。为了让comfyui更加普及，让本地低配置电脑也同样能顺利的运行comfyui，同时避免在comfyui中调用外部API时密钥和地址难以统一管理，以及许多更优秀模型本地算力难以支
> L26: ### 目前已支持的节点

## 星数曲线

```mermaid
xychart-beta
    title "MoJIeAIGC/comfyui-MJAPI-party 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-25 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `0707ac85389d` · [字段定义](../../DATASET.md)*
